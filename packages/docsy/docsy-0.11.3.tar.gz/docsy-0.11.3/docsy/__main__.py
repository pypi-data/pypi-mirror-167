import os,shutil

PATH=__file__[:-10]
pthr=os.environ.get("PATH")

pth=__file__[:-10].split('/')
if pth==[__file__[:-9]]:
    pth=__file__[:-9].split('\\')
#print(pth[-2],__file__[:-9][:-len(pth[-2])-1])
#print(PATH)
#os.system("cd "+PATH)
os.system("git init")
sitename=""

def update(repo):
    os.system(f"cd {sitename} && git remote add origin "+repo)
    os.system(f"cd {sitename} && git add .")
    os.system(f"cd {sitename} && git commit -m 'init'")
    os.system(f"cd {sitename} && git checkout -b docs")
    os.system(f"cd {sitename} && git push origin docs")
    
def serve(sitenamee):
    print(f"{sitenamee}/public/")
    os.system(f"cd {sitenamee}/public/ && python -m http.server 2000")
    #os.system("cd")

def init(stname):
    os.system(f"git clone https://github.com/ginoblog/docsy-init.git {stname}/")
    if not ("Git" in pthr):
        print("DOCSY: Git clone failed, copying data instead.")
        
        shutil.copytree(__file__[:-11]+"sample\\",stname+"\\")
def _help():
    stri="""
      Docsy v 0.11.1
    Docsy is a docs site generator written with python.
    
    Usage:
        python -m docsy <command> [sitename]
        
    Commands:
        init    |    Build a new site cloned with git (from docsy-init)
        server  |    Run test server on localhost:2000 to test your site
        render  |    Render and generate static files from the docs
        clean   |    Clear public folder
        help    |    Help with commands
        
    More information please see https://docsy.inet2.org
        
    """
    print(stri)
import sys
#print(sys.argv)
if len(sys.argv)==1:
    _help()
    print("DOCSY: Error: No command specified")
elif sys.argv[1]=="init":
    if len(sys.argv)<=2:
        print("DOCSY: Error: No sitename specified.")
    else:
        try:
            init(sys.argv[2])
            sitename=sys.argv[2]
        except Exception as er:
            print("DOCSY: Unknown error:",er)
elif sys.argv[1]=="server":
    if len(sys.argv)<=2:
        print("DOCSY: Error: No sitename specified.")
    else:
        sitename=sys.argv[2]
        os.system(f"python {sitename}/scripts/render.py") 
        try:
            serve(sitename)
        except KeyboardInterrupt:
            print("DOCSY: Recieved Keyboard Interrupt, quitting ......")
elif sys.argv[1]=="render":
    if len(sys.argv)<=2:
        print("DOCSY: Error: No sitename specified.")
    else:
        sitename=sys.argv[2]
        os.system(f"python {sitename}/scripts/render.py")  
        os.system(f"python {sitename}/scripts/search.py")  

elif sys.argv[1]=="clean":
    if len(sys.argv)<=2:
        print("DOCSY: Error: No sitename specified.")
    else:
        try:
            shutil.rmtree(__file__[:-17]+"public/")
        except:
            print("DOCSY: Public already cleaned!")
            
elif sys.argv[1]=="help":
    _help()
    
else:
    _help()
    print("DOCSY: Error: Invalid command")