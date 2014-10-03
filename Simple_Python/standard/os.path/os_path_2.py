import os
import os.path

os.chdir("/tmp")
for path in [".",
             "..",
             "./one/two/three/four",
             "../one/two/three/four",
             ]:
    print "%17s:'%s'"%(path,os.path.abspath(path))
