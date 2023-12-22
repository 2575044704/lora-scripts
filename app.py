import os
import subprocess
import sys
ngrok_use = True
def ngrok_start(port: int, address_name: str, should_run: bool):
    if not should_run:
        print('Skipping ngrok start')
        return
        ngrokToken = '2YteSlIvArBGFgXx70rY6MN1ThW_gUnTwjXzT5kbnNozZFL2'
        print('use nrgok')
        from pyngrok import conf, ngrok
        conf.get_default().auth_token = ngrokToken
        conf.get_default().monitor_thread = False
        ssh_tunnels = ngrok.get_tunnels(conf.get_default())
        if len(ssh_tunnels) == 0:
            ssh_tunnel = ngrok.connect(port, bind_tls=True)
            print(f'{address_name}：' + ssh_tunnel.public_url)
        else:
            print(f'{address_name}：' + ssh_tunnels[0].public_url)
    else:
        print('skip start ngrok')
def install_and_run_jupyterlab(port=7860):
    try:
        # 安装JupyterLab
        subprocess.run([sys.executable, "-m", "pip", "install", "jupyterlab"], check=True)
        print("JupyterLab has been successfully installed.")

        # 运行JupyterLab，指定端口
        subprocess.run([sys.executable, "-m", "jupyter", "notebook", "--port", str(port)], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # 指定端口号，例如 7860
    ngrok_start(7860,'7860',ngrok_use)
    desired_port = 7860
    install_and_run_jupyterlab(port=desired_port)

#os.chdir(f"/home/xlab-app-center")
#os.system('bash install.bash')
#os.system('bash run.sh --port 7860')
