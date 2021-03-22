# saxon-flask-api

## How to use this repo

1. Make venv `python3 -m venv env`
2. activate your virtual environemnt `source env/bin/activate`
3. Install requirements `pip install -r requirements.txt`
5. Run uwsgi server `uwsgi -i uwsgi.ini`
6. Check console for no errors.
7. Run the stresstest `python stresstest.py` in a second terminal.

After the stresstest completes (20k calls to the local api) go check the logs of the uwsgi server. It should look something like this:

```
JET RUNTIME HAS DETECTED UNRECOVERABLE ERROR: runtime error
mmap() failed (errno=ENOMEM).
It may be related to exceeding process's maximum number of memory mappings
Please try to adjust VM params by setting the following VM options:
  export JETVMPROP="-Djet.gc.defrag.holes.threshold=60815 -Djet.gc.force.defrag.to.lower.address" 

If this doesn't help, please try to increase the limit of memory mappings by running the following command in terminal as root:

  sysctl -w vm.max_map_count=131060

(default value is most likely around 65530).
Please note that this setting is not persistent and will be reseted to default after reboot
If it helps, you can make it persistent by adding 'vm.max_map_count=131060' line to /etc/sysctl.conf

Please, contact the vendor of the application.
Core dump will be piped to "/usr/share/apport/apport %p %s %c %d %P %E"
Extra information about error is saved in the "jet_err_223170.txt" file.

DAMN ! worker 1 (pid: 223170) died, killed by signal 6 :( trying respawn ...
Respawned uWSGI worker 1 (new pid: 224389)
```