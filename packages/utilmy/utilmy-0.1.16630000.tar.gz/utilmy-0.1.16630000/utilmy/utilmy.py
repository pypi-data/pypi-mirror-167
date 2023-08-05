# -*- coding: utf-8 -*-
""" Main entry



"""
import os, sys, time, datetime,inspect, json, yaml, gc, random
from tkinter import E
from box import Box


#### Typing ######################################################################################
## https://www.pythonsheets.com/notes/python-typing.html
### from utilmy import (  )
from typing import List, Optional, Tuple, Union, Dict, Any
Dict_none = Union[dict, None]
List_none = Union[list, None]
Int_none  = Union[None,int]
Path_type = Union[str, bytes, os.PathLike]

try:
    import numpy.typing
    npArrayLike = numpy.typing.ArrayLike
except ImportError:
    npArrayLike = Any







###################################################################################################
global verbose
def get_verbosity(verbose:int=None):
    """function get_verbosity
    """
    if verbose is None :
        verbose = os.environ.get('utilmy-verbose', 3)
    return verbose
verbose = get_verbosity()   ### Global setting


def direpo():
    try :
       import utilmy
       dir_repo1 =  utilmy.__path__[0].replace("\\","/")  + "/"
    except:
       dir_repo1 = os.path.dirname(os.path.abspath(__file__)).replace("\\","/") + "/"
    return dir_repo1





###################################################################################################
def log(*s, **kw):
    print(*s, flush=True, **kw)

def log2(*s, **kw):
    if verbose >=2 : print(*s, flush=True, **kw)

def log3(*s, **kw):
    if verbose >=3 : print(*s, flush=True, **kw)

def loge(*s):
    print(*s,  flush=True)


def help():
    suffix = "\n\n\n###############################"
    ss     = help_create(modulename='utilmy', prefixs=None) + suffix
    log(ss)


###################################################################################################

###################################################################################################
def help_info(fun_name:str="os.system", doprint=True):   
   """  get infos
      
   """ 
   from box import Box 

   fun_name = fun_name.strip()
   fun_name = fun_name.replace(" ", ".")

   if ":"in fun_name :
       x = fun_name.split(":")
       module_name = x[0]
       fun_name    = x[-1]
   else  :
       x           = fun_name.split(".")
       module_name = ".".join(x[:-1])
       fun_name    = x[-1]


   func = import_function(fun_name, module_name, fuzzy_match=True)

   dd = Box({})
   dd.name = fun_name
   # dd.args = help_signature(func)   
   dd.args = help_get_funargs(func)      
   dd.doc  = help_get_docstring(func)
   dd.code = help_get_codesource(func)

   try :
        ss = ""
        for l in dd.args:
            l  = l.split("=")  
            if len(l)> 1:
                ss = ss + f"'{l[0]}': {l[1]}"  +","
            else :
                ss = ss + l +","    
        dd.args2 = "{" + ss[:-1]  + "}"
   except :
       dd.args2 = dd.args

   if doprint == 1 or doprint == True :
       log( 'Name: ', "\n",  module_name +"."+ fun_name, "\n" )
       log( 'args:', "\n",  dd.args2, "\n" )
       log( 'doc:',  "\n",  dd.doc, "\n" )
       return ''

   return dd


def help_get_codesource(func):
    """ Extract code source from func name"""
    import inspect
    try:
        lines_to_skip = len(func.__doc__.split('\n'))
    except AttributeError:
        lines_to_skip = 0
    lines = inspect.getsourcelines(func)[0]
    return ''.join( lines[lines_to_skip+1:] )


def help_get_docstring(func):
    """ Extract Docstring from func name"""
    import inspect
    try:
        lines = func.__doc__
    except AttributeError:
        lines = ""
    return lines


def help_get_funargs(func):
    """ Extract Func args  :  (a, b, x='blah') """
    import inspect
    try:
        ll = str( inspect.signature(func) )
        ll = ll[1:-1]
        ll = [ t.strip() for t in ll.split(", ")]

    except :
        ll = ""
    return ll


def help_signature(f):
    """function help_signature
    Args:
        f:   
    Returns:
        
    """
    from collections import namedtuple
    sig = inspect.signature(f)
    args = [
        p.name for p in sig.parameters.values()
        if p.kind == inspect.Parameter.POSITIONAL_OR_KEYWORD
    ]
    varargs = [
        p.name for p in sig.parameters.values()
        if p.kind == inspect.Parameter.VAR_POSITIONAL
    ]
    varargs = varargs[0] if varargs else None
    keywords = [
        p.name for p in sig.parameters.values()
        if p.kind == inspect.Parameter.VAR_KEYWORD
    ]
    keywords = keywords[0] if keywords else None
    defaults = [
        p.default for p in sig.parameters.values()
        if p.kind == inspect.Parameter.POSITIONAL_OR_KEYWORD
        and p.default is not p.empty
    ] or None
    argspec = namedtuple('Signature', ['args', 'defaults',
                                        'varargs', 'keywords'])
    return argspec(args, defaults, varargs, keywords) 


def help_create(modulename='utilmy.nnumpy', prefixs=None):
    """ Extract code source from test code
    """
    if ".py" in modulename :
      modulename = os_module_name(modulename)
         
    import importlib
    prefixs = ['test']
    module1 = importlib.import_module(modulename)
    ll      = dir(module1)
    ll  = [ t for t in ll if prefixs[0] in t]
    ss  = ""
    for fname in ll :
        fun = import_function(fname, modulename)
        ss += help_get_codesource(fun)
    return ss




###################################################################################################
def os_get_dirtmp(subdir=None, return_path=False):
    """ return dir temp for testing,...

    """
    import tempfile
    from pathlib import Path
    dirtmp = tempfile.gettempdir().replace("\\", "/")
    dirtmp = dirtmp + f"/{subdir}/" if subdir is not None else dirtmp
    os.makedirs(dirtmp, exist_ok=True)
    return Path(dirtmp) if return_path  else dirtmp


def os_module_name(filepath=None, mode='importname'):
    try:
        dir1 = os.path.abspath(filepath).replace("\\","/")

        if mode == 'importname':
            dir1 = 'utilmy.' + dir1.split("utilmy/")[-1].replace("/", ".").replace(".py", "")
            return dir1
    except :
        return direpo()


def get_loggers(mode='print', n_loggers=2, verbose_level=None):
    """function get_loggers
    Args:
        mode:   
        n_loggers:   
        verbose_level:   
    Returns:
        
    """
    global verbose
    verbose = get_verbosity(verbose_level)

    if mode == 'print' :
        ttuple = [log]
        if n_loggers >=  2:    ttuple.append(log2)
        if n_loggers >=  3:    ttuple.append(log3)
        return tuple(ttuple)


#### Universal config Loader
from utilmy.configs.util_config import config_load


###################################################################################################
def to_file(txt, fpath, mode='a'):
    with open(fpath, mode=mode) as fp:
        fp.write(txt)


def find_fuzzy(word:str, wlist:list, threshold=0.0):
  """ Find closest fuzzy string
        ll = dir(utilmy)
        log(ll)
        find_fuzzy('help create fun arguu', ll)  
  """  
  # import numpy as np   
  from difflib import SequenceMatcher as SM
  scores = [ SM(None, str(word), str(s2) ).ratio() for s2 in wlist  ]
  #log(scores)
  # imax = np.argmax(scores)  
  imax = max(range(len(scores)), key=scores.__getitem__)

  if scores[imax] > threshold :
      most_similar = wlist[imax]
      return most_similar
  else : 
      raise Exception( f'Not exist {word}  ; {wlist} ' )   


def import_function(fun_name=None, module_name=None, fuzzy_match=False):
    """function import_function
    Args:
        fun_name:   
        module_name:   
        fuzzy_match:   
    Returns:
        
    """
    import importlib

    try :
        if isinstance(module_name, str):
          module1 = importlib.import_module(module_name)
          if fuzzy_match: fun_name = find_fuzzy(fun_name, dir(module1) )
          func = getattr(module1, fun_name)
        else :
          func = globals()[fun_name]
        return func
    except Exception as e :
        msg = "Missing " + str(fun_name) + "," + str(dir(module1))
        raise Exception( msg )  


from utilmy.oos import glob_glob




def sys_exit(msg="exited",  err_int=0):
    """function sys_exit
    Args:
        msg:   
        err_int:   
    Returns:
        
    """
    import os, sys
    log(msg)         
    ### exit with no error msg 
    # sys.stderr = open(os.devnull, 'w')
    sys.stdout = sys.__stdout__ = open(os.devnull, 'w')
    sys.exit(err_int)         

    
def sys_install(cmd=""):
   """function sys_install
   Args:
       cmd:   
   Returns:
       
   """
   import os, sys, time  
   log("Installing  ")
   log( cmd +"  \n\n ...") ; time.sleep(7)
   os.system(cmd )
   log( "\n\n\n############### Please relaunch python  ############## \n")   
   log('Exit \n\n\n')


def pip_install(pkg_str=" pandas "):
    """
        try:
        import pandas as pd
    except ImportError:
        
    finally:
        import pandas as pd

    """    
    import subprocess, sys
    clist = [sys.executable, "-m", "pip", "install",  ]  + pkg_str.split(" ")
    log("Installing", pkg_str)
    subprocess.check_call(clist)


def sys_path_append(path="__file__", level_above=2):
   """ Add parent folder as path for import """ 
   import sys,os

   fi   = os.path.abspath(path)
   diri = os.path.dirname(fi)
   for i in range(1,level_above):
       diri = os.path.join(os.path.dirname(fi),os.pardir)

   sys.path.append(diri)



def load_function_uri(uri_name: str="MyFolder/myfile.py:my_function"):
    """ Load dynamically Python function/Class from string name
    Doc::

        ###### Pandas CSV case : Custom MLMODELS One
        #"dataset"        : "mlmodels.preprocess.generic:pandasDataset"

        ###### External File processor :
        #"dataset"        : "MyFolder/preprocess/myfile.py:pandasDataset"
    """
    import importlib, sys
    from pathlib import Path
    if ":" in uri_name :
        pkg = uri_name.split(":")
        assert len(pkg) > 1, "  Missing :   in  uri_name module_name:function_or_class "
        package, name = pkg[0], pkg[1]

    else :
        pkg = uri_name.split(".")
        package = ".".join(pkg[:-1])      
        name    = pkg[-1]   

    
    try:
        #### Import from package mlmodels sub-folder
        return  getattr(importlib.import_module(package), name)

    except Exception as e1:
        try:
            ### Add Folder to Path and Load absoluate path module
            path_parent = str(Path(package).parent.parent.absolute())
            sys.path.append(path_parent)
            #log(path_parent)

            #### import Absolute Path model_tf.1_lstm
            model_name   = Path(package).stem  # remove .py
            package_name = str(Path(package).parts[-2]) + "." + str(model_name)
            #log(package_name, model_name)
            return  getattr(importlib.import_module(package_name), name)

        except Exception as e2:
            raise NameError(f"Module {pkg} notfound, {e1}, {e2}")



### Generic Date function   #####################################################
def date_now(datenow:Union[str,int,datetime.datetime]="", fmt="%Y%m%d",
             add_days=0,  add_mins=0, add_hours=0, add_months=0,
             timezone='Asia/Tokyo', fmt_input="%Y-%m-%d",
             force_dayofmonth=-1,   ###  01 first of month
             force_dayofweek=-1,
             force_hourofday=-1,
             returnval='str,int,datetime/unix'):
    """ One liner for date Formatter
    Doc::

        datenow: 2012-02-12  or ""  emptry string for today's date.
        fmt:     output format # "%Y-%m-%d %H:%M:%S %Z%z"
        date_now(timezone='Asia/Tokyo')    -->  "20200519"   ## Today date in YYYMMDD
        date_now(timezone='Asia/Tokyo', fmt='%Y-%m-%d')    -->  "2020-05-19"
        date_now('2021-10-05',fmt='%Y%m%d', add_days=-5, returnval='int')    -->  20211001
        date_now(20211005, fmt='%Y-%m-%d', fmt_input='%Y%m%d', returnval='str')    -->  '2021-10-05'
        date_now(20211005,  fmt_input='%Y%m%d', returnval='unix')    -->  1634324632848
    """
    from pytz import timezone as tzone
    import datetime, time

    if isinstance(datenow, datetime.datetime):
        now_utc = datenow

    elif len(str(datenow)) >7 :  ## Not None
        now_utc = datetime.datetime.strptime(str(datenow), fmt_input)
    else:
        now_utc = datetime.datetime.now(tzone('UTC'))  # Current time in UTC

    #### Force dates
    if force_dayofmonth >0 :
        now_utc = now_utc.replace(day=force_dayofmonth)

    if force_dayofweek >0 :
        # https://stackoverflow.com/questions/25426919/python-construct-datetime-having-weekday-with-other-time-parameters
        #from datetime import timedelta
        #monday = today - datetime.timedelta(days= now_utc.weekday())
        #result = (monday + timedelta(days=weekday)).replace(hour=int(t), minutes=int((t - int(t)) * 60))
        pass

    if force_hourofday >0 :
        now_utc = now_utc.replace(hour=force_hourofday)


    now_new = now_utc.astimezone(tzone(timezone))  if timezone != 'utc' else  now_utc.astimezone(tzone('UTC'))
    now_new = now_new + datetime.timedelta(days=add_days, hours=add_hours, minutes=add_mins,)


    if add_months>0 :
        pass

    if   returnval == 'datetime': return now_new ### datetime
    elif returnval == 'int':      return int(now_new.strftime(fmt))
    elif returnval == 'unix':     return time.mktime(now_new.timetuple())
    else:                         return now_new.strftime(fmt)



### Generic Glob  #################################################################################
from utilmy.oos import  glob_glob


from utilmy.util_download import google_download, download_google


###################################################################################################
def pd_random(ncols=7, nrows=100):
   """function pd_random
   Args:
       ncols:   
       nrows:   
   Returns:
       
   """
   import pandas as pd
   ll = [[ random.random() for i in range(0, ncols)] for j in range(0, nrows) ]
   df = pd.DataFrame(ll, columns = [str(i) for i in range(0,ncols)])
   return df


def pd_generate_data(ncols=7, nrows=100):
    """ Generate sample data for function testing categorical features
    """
    import numpy as np, pandas as pd
    np.random.seed(444)
    numerical    = [[ random.random() for i in range(0, ncols)] for j in range(0, nrows) ]
    df = pd.DataFrame(numerical, columns = [str(i) for i in range(0,ncols)])
    df['cat1']= np.random.choice(  a=[0, 1],  size=nrows,  p=[0.7, 0.3]  )
    df['cat2']= np.random.choice(  a=[4, 5, 6],  size=nrows,  p=[0.5, 0.3, 0.2]  )
    df['cat1']= np.where( df['cat1'] == 0,'low',np.where(df['cat1'] == 1, 'High','V.High'))
    return df


def pd_getdata(verbose=True):
    """data = test_get_data()
    df   = data['housing.csv']
    df.head(3)
    https://github.com/szrlee/Stock-Time-Series-Analysis/tree/master/data
    """
    import pandas as pd
    flist = [
        'https://raw.githubusercontent.com/samigamer1999/datasets/main/titanic.csv',
        'https://github.com/subhadipml/California-Housing-Price-Prediction/raw/master/housing.csv',
        'https://raw.githubusercontent.com/AlexAdvent/high_charts/main/data/stock_data.csv',
        'https://raw.githubusercontent.com/samigamer1999/datasets/main/cars.csv',
        'https://raw.githubusercontent.com/samigamer1999/datasets/main/sales.csv',
        'https://raw.githubusercontent.com/AlexAdvent/high_charts/main/data/weatherdata.csv'
    ]
    data = {}
    for url in flist :
       fname =  url.split("/")[-1]
       log( "\n", "\n", url, )
       df = pd.read_csv(url)
       data[fname] = df
       if verbose: log(df)
       # df.to_csv(fname , index=False)
    log(data.keys() )
    return data


class Index0(object):
    """
    ### to maintain global index, flist = index.read()  index.save(flist)
    """
    def __init__(self, findex:str="ztmp_file.txt"):
        """ Index0:__init__
        Args:
            findex (function["arg_type"][i]) :     
        Returns:
           
        """
        self.findex = findex
        log(os.path.dirname(self.findex))
        os.makedirs(os.path.dirname(self.findex), exist_ok=True)
        if not os.path.isfile(self.findex):
            with open(self.findex, mode='a') as fp:
                fp.write("")              

    def read(self,):            
        """ Index0:read
        Args:
            :     
        Returns:
           
        """
        with open(self.findex, mode='r') as fp:
            flist = fp.readlines()

        if len(flist) < 1 : return []    
        flist2 = []
        for t  in flist :
            if len(t) > 5 and t[0] != "#"  :
              flist2.append( t.strip() )
        return flist2    

    def save(self, flist:list):
        """ Index0:save
        Args:
            flist (function["arg_type"][i]) :     
        Returns:
           
        """
        if len(flist) < 1 : return True
        ss = ""
        for fi in flist :
          ss = ss + str(fi) + "\n"        
        # log(ss)        
        with open(self.findex, mode='a') as fp:
            fp.write(ss )
        return True   



###################################################################################################
###### Pandas #####################################################################################
from utilmy.parallel import (
    pd_read_file,    ### parallel reading
    pd_read_file2,
    pd_groupby_parallel,
)



from utilmy.ppandas import (
    pd_random,
    pd_merge,
    pd_plot_multi,
    pd_plot_histogram,
    pd_filter,
    pd_to_file,
    pd_sample_strat,
    pd_cartesian,
    pd_col_bins,
    pd_dtype_reduce,
    pd_dtype_count_unique,
    pd_dtype_to_category,
    pd_dtype_getcontinuous,
    pd_del,
    pd_add_noise,
    pd_cols_unique_count,
    pd_show,
    pd_to_hiveparquet,
    pd_to_mapdict
)




#########################################################################################################
##### Utils numpy, list #################################################################################
#from utilmy.keyvalue import  (
#   diskcache_load,
#   diskcache_save,
#   diskcache_save2,
#   db_init, db_size, db_flush
#)



###################################################################################################
###### Parallel #####################################################################################
from utilmy.parallel import (
    multithread_run,
    multiproc_run
)




###################################################################################################
####### Numpy compute #############################################################################
from utilmy.nnumpy import (

    dict_to_namespace,
    to_dict,
    to_timeunix,
    to_datetime,
    np_list_intersection,
    np_add_remove,
    to_float,
    to_int,
    is_int,
    is_float

)



##### OS, cofnfig ######################################################################################
from utilmy.oos import(
    os_path_size,
    os_path_split,
    os_file_check,
    os_file_replacestring,
    os_walk,
    z_os_search_fast,
    os_search_content,
    os_get_function_name,
    os_variable_exist,
    os_variable_init,
    os_import,
    os_variable_check,
    os_clean_memory,
    os_system_list,
    os_to_file,
    os_platform_os,
    os_platform_ip,
    os_memory,
    os_sleep_cpu,
    os_cpu,
    # os_ram_object,
    os_copy,
    os_removedirs,
    os_getcwd,
    os_system,
    os_makedirs,
    
    toFileSafe
)

### Alias
os_remove = os_removedirs
#to_file   = os_to_file



################################################################################################
########  Configuration  #######################################################################
from utilmy.configs.util_config import (
 config_load,
 global_verbosity


)


######################################################################################################
######## External IO #################################################################################

######################################################################################################
###### Plot ##########################################################################################
#from utilmy.viz.vizhtml import (
#  images_to_html,   ### folder of images to HTML
#  test_getdata
# )



###################################################################################################
###### Debug ######################################################################################
from utilmy.debug import (
    print_everywhere,

    log10,
    log_trace,  ###(msg="", dump_path="", globs=None)  Debug with full trace message


    profiler_start,
    profiler_stop
)



######################################################################################################
########Git ##########################################################################################
def git_repo_root():
    """function git_repo_root
    Args:
    Returns:
        
    """
    try :
      cmd = "git rev-parse --show-toplevel"
      mout, merr = os_system(cmd)
      path = mout.split("\n")[0]
      if len(path) < 1:  return None
    except : return None
    return path


def git_current_hash(mode='full'):
    """function git_current_hash
    Args:
        mode:   
    Returns:
        
    """
    import subprocess
    label = None
    try:
        # label = subprocess.check_output(["git", "describe", "--always"]).strip();
        label = subprocess.check_output([ 'git', 'rev-parse', 'HEAD' ]).strip()
        label = label.decode('utf-8')
    except Exception as e:
        log('Error get git hash')
        label=  None
    return label




################################################################################################
################################################################################################
class Session(object) :
    """ Save Python Interpreter session on disk
      from util import Session
      sess = Session("recsys")
      sess.save( globals() )
    """
    def __init__(self, dir_session="ztmp/session/",) :
      """ Session:__init__
      Args:
          dir_session:     
          :     
      Returns:
         
      """
      os.makedirs(dir_session, exist_ok=True)
      self.dir_session =  dir_session
      self.cur_session =  None
      log(self.dir_session)

    def show(self) :
       """ Session:show
       Args:
       Returns:
          
       """
       import glob
       flist = glob.glob(self.dir_session + "/*" )
       log(flist)

    def save(self, name, glob=None, tag="") :
       """ Session:save
       Args:
           name:     
           glob:     
           tag:     
       Returns:
          
       """
       path = f"{self.dir_session}/{name}{tag}/"
       self.cur_session = path
       os.makedirs(self.cur_session, exist_ok=True)
       self.save_session(self.cur_session, glob)

    def load(self, name, glob:dict=None, tag="") :
      """ Session:load
      Args:
          name:     
          glob (function["arg_type"][i]) :     
          tag:     
      Returns:
         
      """
      path = f"{self.dir_session}/{name}{tag}/"
      self.cur_session = path
      log(self.cur_session)
      self.load_session(self.cur_session , glob )


    def save_session(self, folder , globs, tag="" ) :
      """ Session:save_session
      Args:
          folder:     
          globs:     
          tag:     
      Returns:
         
      """
      import pandas as pd
      os.makedirs( folder , exist_ok= True)
      lcheck = [ "<class 'pandas.core.frame.DataFrame'>", "<class 'list'>", "<class 'dict'>",
                 "<class 'str'>" ,  "<class 'numpy.ndarray'>" ]
      lexclude = {   "In", "Out", "get_ipython", 'exit','quit', 'Session',  }
      gitems = globs.items()
      for x, _ in gitems :
         if not x.startswith('_') and  x not in lexclude  :
            x_type =  str(type(globs.get(x) ))
            fname  =  folder  + "/" + x + ".pkl"
            try :
              if "pandas.core.frame.DataFrame" in x_type :
                  pd.to_pickle( globs[x], fname)

              elif x_type in lcheck or x.startswith('clf')  :
                  save( globs[x], fname )

              log(fname)
            except Exception as e:
                  log(x, x_type, e)


    def load_session(self, folder, globs=None) :
      """
      """
      log(folder)
      for dirpath, subdirs, files in os.walk( folder ):
        for x in files:
           filename = os.path.join(dirpath, x)
           x = x.replace(".pkl", "")
           try :
             globs[x] = load(  filename )
             log(filename)
           except Exception as e :
             log(filename, e)


def save(dd, to_file="", verbose=False):
  """function save
  Args:
      dd:   
      to_file:   
      verbose:   
  Returns:
      
  """
  import pickle, os
  os.makedirs(os.path.dirname(to_file), exist_ok=True)
  pickle.dump(dd, open(to_file, mode="wb") , protocol=pickle.HIGHEST_PROTOCOL)
  #if verbose : os_file_check(to_file)


def load(to_file=""):
  """function load
  Args:
      to_file:   
  Returns:
      
  """
  import pickle
  dd =   pickle.load(open(to_file, mode="rb"))
  return dd






###################################################################################################
###### Test #######################################################################################
def test_all():
    """function test_all
    """
    test1()
    test2()
    test3()
    test4()
    test5()


def test1():
    import utilmy as m

    ###################################################################
    log("\n##### git_repo_root  ", m.git_repo_root())
    assert not m.git_repo_root() == None, "err git repo"

    log("\n##### git_current_hash  ", m.git_current_hash())
    assert not m.git_current_hash() == None, "err git hash"


    ####################################################################
    log("\n##### global_verbosity  ")
    log('verbosity', m.global_verbosity(__file__, "config.json", 40,))
    log('verbosity', m.global_verbosity('../', "config.json", 40,))
    log('verbosity', m.global_verbosity(__file__))

    verbosity = 40
    gverbosity = m.global_verbosity(__file__)
    assert gverbosity == 5, "incorrect default verbosity"
    gverbosity =m.global_verbosity(__file__, "config.json", 40,)
    assert gverbosity == verbosity, "incorrect verbosity "

    ################################################################################################


def test2():
    import utilmy as m

    log('#### Index0')
    d0 = os_get_dirtmp()    
    file_name = f"{d0}/test_file_{int(time.time())}.txt"
    index = m.Index0(file_name)

    # 2 save some data
    data = [ "testestest", 2, 'for ii in rnage zz', '#comment',]
    output = [ 'testestest', 'for ii in rnage zz', ]
    index.save(data)

    assert index.read() == output, 'FAILED, -> get data wrong'


def test3():
    import utilmy as m

    log('#### Session')
    d0 = os_get_dirtmp()
    folder_name = f"{d0}/session"

    session = m.Session(folder_name)
    log(session)

    # save session
    glob = {'test': 'qwe rty yui'}
    res = session.save(name='session1', glob=glob)

    glob2 = {'test': 'nothing here'}
    res = session.load(name='session1', glob=glob2)
    
    assert glob2 == glob, 'FAILED, -> session error'


def test4():
    import utilmy as m


    def test_func(arg1, arg2):
        """HELP doc string
        """
        return arg1 + arg2


    for name in [ 'utilmy.parallel', 'utilmy.utilmy',  ]:
        log("\n####", name,"\n", m.help_create(name))
        assert m.help_create(name), 'FAILED -> help_create'
        log("\n####", name,"\n", m.help_info(name))
        assert m.help_create(name), 'FAILED -> help_info'

    log("\n####", m.help_get_codesource(func=test_func))
    assert m.help_get_codesource(func=test_func), 'FAILED -> help_get_codesource'

    log("\n####", m.help_get_docstring(func=test_func))
    assert m.help_get_docstring(func=test_func), 'FAILED -> help_get_docstring'

    log("\n####", m.help_get_funargs(func=test_func))
    assert m.help_get_funargs(func=test_func), 'FAILED -> help_get_funargs'

    log("\n####", m.help_signature(f=test_func))
    assert m.help_signature(f=test_func), 'FAILED -> help_signature'


def test5():
    import utilmy as m

    drepo = direpo()

    log("\n####", m.os_get_dirtmp)
    assert m.os_get_dirtmp(), 'FAILED -> os_get_dirtmp'
    assert m.os_get_dirtmp(subdir='test'), 'FAILED -> os_get_dirtmp'
    assert m.os_get_dirtmp(subdir='test', return_path=True), 'FAILED -> os_get_dirtmp'


    log("\n####", m.os_module_name(filepath='utilmy/utilmy.py'))
    assert m.os_module_name(filepath=drepo + 'utilmy/utilmy.py'), 'FAILED -> os_module_name'


    log("\n####", m.get_loggers())
    log("\n####", m.get_loggers(n_loggers=3))

    log("\n####", m.import_function(fun_name='test3', module_name='utilmy'))
    assert m.import_function(fun_name='test3', module_name='utilmy'), 'FAILED -> import_function'


    uri_name = drepo + "utilmy/utilmy.py:test2"
    myclass = load_function_uri(uri_name)
    log(myclass)
    assert myclass, 'FAILED -> load_function_uri'



def test6():
    import utilmy as m

    log("\n####", date_now)

    assert m.date_now(timezone='Asia/Tokyo')    #-->  "20200519"   ## Today date in YYYMMDD
    assert m.date_now(timezone='Asia/Tokyo', fmt='%Y-%m-%d')    #-->  "2020-05-19"
    assert m.date_now('2021-10-05',fmt='%Y%m%d', add_days=-5, returnval='int')  == 20211001   #-->  20211001
    assert m.date_now(20211005, fmt='%Y-%m-%d', fmt_input='%Y%m%d', returnval='str') == '2021-10-05'    #-->  '2021-10-05'
    assert m.date_now(20211005,  fmt_input='%Y%m%d', returnval='unix')   == 1634324632848  #-->  1634324632848




###################################################################################################
if __name__ == "__main__":
    import fire
    fire.Fire()




