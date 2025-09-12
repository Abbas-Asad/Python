import os
import subprocess

# Projects folder ka path
projects_dir = r"C:\Users\Lenovo\Desktop\Python\projects-experimental-2\streamlit"

# Har sub-folder (project) ke liye loop
for project in os.listdir(projects_dir):
    project_path = os.path.join(projects_dir, project)

    if os.path.isdir(project_path):  # sirf folders
        print(f"📦 Generating requirements.txt for: {project}")
        try:
            # pipreqs se requirements.txt generate karo
            subprocess.run(["pipreqs", project_path, "--force"], check=True)
            print(f"✅ Done: {project_path}\\requirements.txt")
        except Exception as e:
            print(f"❌ Failed for {project}: {e}")
