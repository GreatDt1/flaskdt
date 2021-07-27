from flask import render_template

class FlaskDt():
    def __init__(self, app, db, template, route):
        self.app = app
        self.db = db
        self.template = template
        self.route = route
    
    @property
    def display_table(self):
        def wrapper_1(*args, **kwargs):

            @self.app.route(f'/{self.route}/<string:tablename>', methods=['POST', 'GET'])
            def table_page(tablename):
                
                if tablename == "":
                    return "No table name has been provided"

                table_class = get_class_by_tablename(tablename, self.db)

                if table_class:
                    columns = table_class.__table__.columns.keys()
                    records = self.db.session.query(table_class).all()

                    return render_template(self.template, columns=columns, records=records, tablename=tablename)

                else:
                    return f'No such table {tablename} in the database. Try creating the table'
                        
    
        return wrapper_1

    # need to define a decorator for the app instance in the FlaskDt instance
    

def get_class_by_tablename(tablename, db):
    """Return class reference mapped to table.

    :param tablename: String with name of table.
    :return: Class reference or None.
    """
    for c in db.Model._decl_class_registry.values():
        if hasattr(c, '__tablename__') and c.__tablename__ == tablename:
            return c

    # This sort of prints the schema
    # for t in db.metadata.tables.items():
    #         print(t)

    # print(get_class_by_tablename("products"))