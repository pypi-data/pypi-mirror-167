import argparse
import os
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("name")
    parser.add_argument("age")

    args = parser.parse_args()
    if args.name == "create_app":
        print(f"================CREATING {args.age} App===================================")
        print(os.getcwd())
        curr = os.getcwd()
        # get file paths, joining
        static = os.path.join(curr,f"{args.age}","static")
        app_config = os.path.join(curr,f"{args.age}","libs")
        app_js = os.path.join(curr,f"{args.age}","static",f"{args.age}","js")
        app_css = os.path.join(curr,f"{args.age}","static",f"{args.age}","css")
        app_html = os.path.join(curr,f"{args.age}","static",f"{args.age}","templates")
        os.mkdir(os.path.join(curr,f"{args.age}"))
        dirs = [static,app_config,app_js,app_css,app_html]
        for dir_ in dirs:
            os.makedirs(dir_)
        # creating the files
        app_js_ = os.path.join(curr,f"{args.age}","static",f"{args.age}","js",f"{args.age}.js")
        app_css_ = os.path.join(curr,f"{args.age}","static",f"{args.age}","css",f"{args.age}.css")
        app_html_ = os.path.join(curr,f"{args.age}","static",f"{args.age}","templates",f"{args.age}.html")
        dirs = [app_js_,app_css_,app_html_]
        for dir_ in dirs:
            with open(dir_,"w") as f:
                f.write("")
        file_py = os.path.join(curr,f"{args.age}","app.py")
        file_json = os.path.join(curr,f"{args.age}","app.json")
        file_init = os.path.join(curr,f"{args.age}","__init__.py")
        file_read = os.path.join(curr,f"{args.age}","read_this_file_for_help.py")
        with open(file_py,"w") as f:
            f.write("#test 123")
        with open(file_json,"w") as f:
            f.write("{ \n }")
        with open(file_init,"w") as f:
            f.write(f"# ======================= {args.age} App============================")
        with open(file_read,"w") as f:
            f.write(f"# ============READ THIS FILE TO GET MORE HELP ======================")
        
        print(f"================CREATED {args.age} APP SUCCESSFULLY=======================")

    print(f"args === {args}, age==={args.name}")

main()