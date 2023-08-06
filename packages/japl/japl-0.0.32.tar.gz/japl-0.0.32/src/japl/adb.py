from pandas import DataFrame, concat
from typing import List, Callable
from tqdm import tqdm
from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
from .exceptions import ParameterTypingException
sc = SparkContext.getOrCreate()
spark = SparkSession(sc)
try:
    # up to DBR 8.2
    from dbutils import DBUtils as dbutils  # pylint: disable=import-error,wrong-import-position
    NEW_DBUTILS = False
except:
    # above DBR 8.3
    from dbruntime.dbutils import DBUtils as dbutils  # pylint: disable=import-error,wrong-import-position
    NEW_DBUTILS = True

from .exceptions import EmptyDataFrameException
from .decoradores import Singleton

@Singleton
class DeltaManager:
    """
    The DeltaManager helps you manage your Delta Tables and operate
    over them.

    Attributes:
        tables (DataFrame): A register with all the mounted tables and 
        some extra info about them.
    """
    def __init__(self, mounts = ["raw", "silver", "gold"]):
        # Inicializamos el dataframe de registro
        self.tables = None
        self.update()
        
    def mount(self, 
              storage:     str,
              key:         str,
              mount_point: str       = '/mnt/',
              mounts:      List[str] = ["raw", "silver", "gold"], 
              postfix:     str       = '-zone',
              include_tqdm:        bool      = False
              ):
        """
        Mounts a set of zones into the system.

        Args:
            storage (str): The name of the storage to mount. This can be found at keys access in your storage account.
            key (str): The key of the storage to mount. This can be found at keys access in your storage account.
            mount_point (str, optional): The mount point to use. 
                Defaults to '/mnt/'.
            mounts (List[str], optional): A list of all the mounts you want. This doesn't include the prefix. Check example. 
                Defaults to ["raw", "silver", "gold"].
            postfix (str, optional): The postfix is the ending you want to put to your mount zones. Set it to an empty 
            string if you don't want to apply it. 
                Defaults to '-zone'.
            include_tqdm (bool, optional): A flag to include tqdm bars for mounts. 
                Defaults to False.
        """
        def __mount(mount_name: str):
            """
            Mounts a single zone to the system.

            Args:
                mount_name (str): The name of the zone to mount.
            """
            if not f"{mount_point}{mount_name}{postfix}" in list(map(lambda mount: mount.mountPoint, dbutils.fs.mounts())):
                dbutils.fs.mount(
                    source = f"wasbs://{mount_name}{postfix}@{storage}.blob.core.windows.net/",
                    mount_point = f"{mount_point}{mount_name}{postfix}",
                    extra_configs = { 
                        f"fs.azure.account.key.{storage}.blob.core.windows.net": key
                    }
                )

        if include_tqdm:
            list(map(lambda mount_name: __mount(mount_name), tqdm(mounts, desc="Mounts", position=0, leave=True)))
        else:
            list(map(lambda mount_name: __mount(mount_name), mounts))
            
    def update(self):
        nombre_tablas = list(map(lambda table: (table.name, table.database, table.description, table.tableType, table.isTemporary), spark.catalog.listTables()))
        
        self.tables = DataFrame(columns = ['name', 'database', 'path', 'type', 'is_temporary', 'description'])
        
        # Add new ones
        for nombre_tabla in nombre_tablas:
            if not nombre_tabla[0] in self.tables.name.to_list():
                self.tables = concat([self.tables, DataFrame([[nombre_tabla[0], nombre_tabla[1], spark.sql(f"desc formatted {nombre_tabla[0]}").toPandas().set_index("col_name").drop("comment", axis = 1)["data_type"]["Location"], nombre_tabla[3], nombre_tabla[4], nombre_tabla[2]]], columns = ['name', 'database', 'path', 'type', 'is_temporary', 'description'])])
                
    def add(self, 
            table_name:   str,
            raw_path:     str,
            destionation_path: str,
            write_mode:   str  = 'overwrite',
            query:        str  = None,
            transformer        = None,
            file_name:    str  = None,
            nested:       bool = False
            ):
        """
        Creates a new table given a name, a path where the parquet is located and a destination path.

        Args:
            table_name (str): The name of the table.
            
            raw_path (str): The path to the file you want to ingest.
            
            destionation_path (str): The path to the location you want to create the parquet at. 
            
            write_mode (str, optional): Behaviour if the table already exists. Options are 'overwrite' and 'append'. 
                Defaults to 'overwrite'.
            
            query (str, optional): A SQL query to transform the original table. This is applied before the transormer.
            
            transformer (Callable[DataFrame], optional): A function, that takes a Spark DataFrame as a parameter. 
            Return should be a Spark DataFrame. This is executed after the query, so any transformation done by the
            query will affect the input parameter of the transformer.

            file_name (str, optional): The name of the file to inglest. If not specified or None, it will be set
            to the table name as default. 
                Defaults to None.

            nested (bool, optional): A flag that let's the function know if the input is a folder with partitioned data
            or a raw file. True for nested folder, false for raw file. 
                Defaults to False.

        Raises:
            Exception: General Exception to return.
            EmptyDataFrameException: An exception that is thrown when the data to ingest is empty.
        """
        # If the file_name is NOT specified, we set it to table_name
        if not file_name:
            file_name = table_name

        # We read the data from the parquet into a dataframe. 
        if nested:
            df = spark.read.parquet(f"dbfs:{raw_path}{file_name}/{file_name}.parquet")
        else:
            df = spark.read.parquet(f"dbfs:{raw_path}{file_name}.parquet")

        # Filters the data using a SQL query if apply.
        if query:

            df.createOrReplaceTempView(table_name)
            df = spark.sql(query)
            spark.catalog.dropTempView(table_name)

        # The transform function would apply here.
        if transformer:
            if callable(transformer):
                df = transformer(df)
            else:
                ParameterTypingException()

        # We check if there is data in the dataframe.
        if df.count() > 0:
            # Check if the table already exist, then we overwrite it.
            if table_name in [table.name for table in spark.catalog.listTables()]:
                df.write.mode(write_mode).format("delta").option("mergeSchema", "true").saveAsTable(table_name)
            else:
                # In case the table doesn't exist, we create it.
                try:
                    # We write the df in the destionation_path
                    df.write.format('delta').save(destionation_path)
                except Exception as error:
                    EOL = '\n'
                    raise Exception(f'Tried to {write_mode} the table and failed with the following message:{EOL}{error}')
                # Create the table.
                spark.sql("CREATE TABLE " + table_name + " USING DELTA LOCATION " + f"'{destionation_path}{table_name}'" )
        else:
            raise EmptyDataFrameException()
            
        # We update the tables DataFrame.
        self.update()

    def rollback(self,
                 table_name: str, 
                 no_of_versions: int = 1,
                 aim_version: int = None,
                 date: str = None, 
                 timestamp: str = '00:00:00') -> None:
        """
        Rolls back the table. It can take a date or a version as a parameter.

        Args:
            table_name (str): The table to rollback.
            no_of_versions (int, optional): The number of versions to go back in time. Defaults to 1.
            aim_version (int, optional): The version you want to select. Defaults to None.
            date (str, optional): The date you want to rollback to. Defaults to None.
                Format: YYYY-MM-DD
            timestamp (_type_, optional): The time you want to rollback to. Defaults to '00:00:00'.
                Format: HH:MM:SS
        """
        if date:
            spark.sql(f"RESTORE TABLE {table_name} TO TIMESTAMP AS OF '{date} {timestamp}'")
        else:
            if not aim_version:
                current_version = spark.sql(f"DESCRIBE HISTORY {table_name}").toPandas()["version"].max()
                aim_version = current_version - no_of_versions
            
            if aim_version > 0 and aim_version < current_version:
                spark.sql(f"RESTORE TABLE {table_name} TO VERSION AS OF {str(aim_version)}")

    def delete(self, 
               table_name: str):
        """
        Deletes a table from the system. 

        Args:
            table_name (str): The name of the table.
        """
        if table_name in [table.name for table in spark.catalog.listTables()]:
            path = self.tables[self.tables.name == table_name].path.reset_index(drop=True)[0]
            spark.sql(f"DROP TABLE IF EXISTS {table_name}")
            dbutils.fs.rm(f'{path}/{table_name}', recurse=True)
            
    def delete_all(self):
        """
            _summary_
        """
        for table_name in self.tables.name.to_list():
            self.delete(table_name)