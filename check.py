import sys
sys.dont_write_bytecode = True
import pi_instock


t = pi_instock.scrape(False)
t.check()


