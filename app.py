import os
import wandb
import subprocess
import sys

def install_and_run_jupyterlab(port=7860):
    try:
        # 安装JupyterLab
        subprocess.run([sys.executable, "-m", "pip", "install", "jupyterlab"], check=True)
        print("JupyterLab has been successfully installed.")

        # 运行JupyterLab，指定端口
        subprocess.run([sys.executable, "-m", "jupyter", "lab", "--port", str(port)], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # 指定端口号，例如 7860
    desired_port = 7860
    install_and_run_jupyterlab(port=desired_port)

#os.chdir(f"/home/xlab-app-center")
#os.system('bash install.bash')
#os.system('bash run.sh --port 7860')
