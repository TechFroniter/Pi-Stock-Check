import sys
sys.dont_write_bytecode = True
import pi_instock


pi_check = pi_instock.scrape()

pis = pi_check.check()
print(pis)