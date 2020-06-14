from .Database import Database


class DataRepository:
    @staticmethod
    def json_or_formdata(request):
        if request.content_type == 'application/json':
            gegevens = request.get_json()
        else:
            gegevens = request.form.to_dict()
        return gegevens

    @staticmethod
    def meting(componentid, value):
        sql = "INSERT INTO ComponentHistoriek(ComponentID, Waarde) VALUES (%s, %s);"
        params = [componentid, value]
        return Database.execute_sql(sql, params)

    @staticmethod
    def get_componenten():
        sql = "SELECT * from Componenten"
        return Database.get_rows(sql)

    @staticmethod
    def get_componenthistory_by_componentid(componentid):
        sql = "SELECT * FROM ComponentHistoriek WHERE ComponentID = %s"
        params = [componentid]
        return Database.get_rows(sql, params)
    
    @staticmethod
    def get_latest_value(componentid):
        sql = "SELECT Waarde FROM ComponentHistoriek WHERE ComponentID = %s ORDER BY EventID DESC LIMIT 1"
        params = [componentid]
        return Database.get_one_row(sql, params)


