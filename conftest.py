#FIX : Testing file cannot find logic utils - added sys.path.insert to include current directory in path
import sys, os
sys.path.insert(0, os.path.dirname(__file__))