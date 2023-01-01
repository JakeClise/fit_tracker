from mysqlconnection import connectToMySQL

class Activity:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod 
    def get_all_activities(cls):
        query = "SELECT * from activities;"
        results = connectToMySQL('fit_tracker_db').query_db(query)
        activities = []
        for activity in results:
            activities.append(cls(activity))
        return activities
    
    @classmethod
    def save_activity(cls, data):
        query = "INSERT INTO activities (name, description, user_id) VALUES (%(name)s, %(description)s, 1);"
        return connectToMySQL('fit_tracker_db').query_db(query, data)
