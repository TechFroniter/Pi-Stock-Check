import sys
sys.dont_write_bytecode = True
import pi_instock


pi_check = pi_instock.scrape()
pi_check.check()