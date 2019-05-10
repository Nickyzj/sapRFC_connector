bw_monitor_host = 'http://localhost:5000'

from batch_job.switch_env import switch_env

if switch_env == "qcb":
    import rfc_connection.qcb as current_env
    print("Current env: qcb")
elif switch_env == "pcb":
    import rfc_connection.pcb as current_env
    print("Current env: pcb")

user = current_env.user
ashost = current_env.ashost
sysnr = current_env.sysnr
client = current_env.client
passwd = current_env.passwd

