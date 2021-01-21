import ctypes, sys
try:
    try:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin()
    except:
        is_admin = False

    if is_admin:
        import importlib
        import subprocess
        import sys
        import stat
        import glob

        reqs=['colorama', 'tqdm', 'git']
        pipreqs=['colorama', 'tqdm', 'gitpython']
        nfreqs=[]
        for req, pipreq in zip(reqs, pipreqs):
            spam_spec = importlib.util.find_spec(req)
            found = spam_spec is not None
            if found:
                print('Package found: '+req+'\033[m')
            else:
                print('Package missing: '+req+'\033[m')
                nfreqs.append(pipreq)
        print(f'M.I.A Check: {len(reqs)} requeriments, {len(nfreqs)} missing')
        if len(nfreqs)!=0:
            print('Installing missing packages...')
            for nfreq in nfreqs:
                subprocess.check_call([sys.executable, "-m", "pip", "install", nfreq])

        import time
        from colorama import init
        import requests
        from tqdm import tqdm
        from pathlib import Path
        import os
        import shutil
        init()

        os.system('clear')
        print("""   __________________
  |  ______________  |                         ███     
  | | |          | | |                      ░░░ 
Γ-| | |     TK   | | |-ꓶ   █████████████      ████      ██████                  
| | | |   MS  /\ | | | |  ░░███░░███░░███    ░░███     ░░░░░███ 
| | |_|_______\_\|_| | |   ░███ ░███ ░███     ░███      ███████ 
| |        ||        | |   ░███ ░███ ░███     ░███     ███░░███ 
|_|_      _||________|_|   █████░███ █████ ██ █████ ██░░████████
   |____/                 ░░░░░ ░░░ ░░░░░ ░░ ░░░░░ ░░  ░░░░░░░░ 
         """)
        tries=0
        def checkPerm():
            global tries
            perm = input('To continue M.I.A setup needs your permission (Y/N):')
            if perm.upper() == 'Y':
                return None
            elif perm.upper() == 'N':  
                print('\033[1;31mWithout your permission i cant setup MSTK\033[m')
                time.sleep(2)
                exit()
            else:
                print('\033[1;33mPlease try again\033[m')
                tries+=1
                if tries>=5:
                    print('\033[1;31mToo many attempts, closing\033[m')
                    time.sleep(2)
                    exit()
                checkPerm()
        checkPerm()

        reqs=['numpy', 'argparse']
        nfreqs=[]
        for req in reqs:
            spam_spec = importlib.util.find_spec(req)
            found = spam_spec is not None
            if found:
                print('\033[32mPackage found: '+req+'\033[m')
            else:
                print('\033[31mPackage missing: '+req+'\033[m')
                nfreqs.append(req)
        print(f'M.I.A Check: {len(reqs)} requeriments, {len(nfreqs)} missing')
        if len(nfreqs)!=0:
            print('Installing missing packages...')
            for nfreq in nfreqs:
                subprocess.check_call([sys.executable, "-m", "pip", "install", nfreq])
        try:
            subprocess.run(["git"], stdout=subprocess.DEVNULL)
        except FileNotFoundError:
            print('\033[31mGit not installed, please install it and restart the setup.\033[m')
            exit()

        from git import Repo
        try:
            Repo.clone_from('https://github.com/pyjonhact/pyspikon', str(Path.home())+'\pyspikon')
        except:
            print('ERROR: Please delete '+str(Path.home())+'\pyspikon'+' before installing a new version!')
            time.sleep(2)
            exit()
        os.environ['PYTHONPATH']=str(Path.home())+'\pyspikon'
        print('\033[32mSuccessfully installed PySpikon!\033[m')
        time.sleep(2)
        print('Self-destructing')
        for i in tqdm(range(5)):
            print(i, end='\r')
            time.sleep(1)
        os.remove(__file__)

    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
except Exception as e:
    print('An unknown error happened and M.I.A cannot continue the setup, retrying in 2 secs.')
    time.sleep(2)
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)