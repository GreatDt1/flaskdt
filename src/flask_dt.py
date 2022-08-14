from functools import wraps


class FlaskDt():
    def __init__(self, db):
        self.db = db
    

    def display_table(self, func):

        @wraps(func)   
        def get_table(tablename, *args, **kwargs):
            """This function queries all data of a given table given the tablename

            :param tablename: String with name of table called tablename.
            :return: tablename, table_class, columns, records, or none for respective values
            """

            if tablename != "":
                table_class = get_class_by_tablename(tablename, self.db)
                columns=records=None

                if table_class:
                    columns = table_class.__table__.columns.keys()
                    records = self.db.session.query(table_class).all()
                
                return func(tablename=tablename,table_class=table_class,columns=columns,records=records, *args,**kwargs)
            
            return func(*args, **kwargs)
            
        return get_table
    

def get_class_by_tablename(tablename, db):
    """Return class reference mapped to table.

    :param tablename: String with name of table.
    :return: Class reference or None.
    """
    for c in db.Model.registry._class_registry.values():
        if hasattr(c, '__tablename__') and c.__tablename__ == tablename:
            return c
