for i in range(532):
  print("  logicdata[%d] = CHANPIN;" % i)
  print("  INLINE_NOP;")

print("#if defined(__AVR_ATmega328P__) || defined(__AVR_ATmega1280__) || defined(__AVR_ATmega2560__)")
for i in range(532,1024):
  print("  logicdata[%d] = CHANPIN;" % i)
  print("  INLINE_NOP;")
print("#endif")

print("#if defined(__AVR_ATmega1280__) || defined(__AVR_ATmega2560__)")
for i in range(1024,7168):
  print("  logicdata[%d] = CHANPIN;" % i)
  print("  INLINE_NOP;")
print("#endif")
