import requests

response = requests.get("https://gitlab.com/api/v4/users/user_id/projects")
my_projects = response.json()

for project in my_projects:
    print(f"Project Name: {project['name']}/n Project Url: {projects['web_url']}/n")



# from user import User
# from post import Post

# # objects
# app_user_one = User("nn@nn.com", "Nana Janashia", "pwd1", "Dev0ps Engineer")
# app_user_one.get_user_info()

# # app_user_one.change_job_title("Dev0ps Trainer")
# # app_user_one.get_user_info()

# app_user_two = User("j1@nn.com", "Jose Nashia", "pw12", "Engineer")
# app_user_two.get_user_info()
    
# new_post = Post("on a secret mission today", app_user_one.name)
# new_post.get_post_info()

