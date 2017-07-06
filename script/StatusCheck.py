import psutil
import cx_Oracle
import os
import socket
import time

def getSystemStatus():
  ## get Host name
  hostName = socket.gethostname()
  print("Host name: " + hostName)

  ## get CPU usage
#  cpuPercent = psutil.cpu_percent(1)
  cpuPercent = getCPUPercent()
  print("CPU: " + str(cpuPercent))
  
  ## get Memory usage
  memoryPercent = psutil.virtual_memory().percent
  print("Memory: " + str(memoryPercent))

  ## get Disk IO
  ioPercent = getDiskIOPercent()
  
  result = {}
  result['cpuPercent'] = cpuPercent
  result['memoryPercent'] = memoryPercent
  result['ioPercent'] = ioPercent
  result['hostName'] = hostName
  return result

def getDiskIOPercent():

  pipe = os.popen("iostat -xm|awk '{print $12}'|grep '[0-9]'")

  data = pipe.readline()

  lines = data.split('/n')

  maxValue = -1

  for line in lines:
    usage = float(line)
    if maxValue < usage:
      maxValue = usage
  print("Max disk IO: " + str(maxValue))
      
  return maxValue

def getCPUPercent():
  pipe = os.popen("top -n 1|awk '{print $2}'|grep 'us'|cut -d % -f 1")

  data = pipe.readline()

  lines = data.split('/n')

  usage = 0.0
  for line in lines:
    usage = float(line)
  print("Max disk IO: " + str(usage))

  return usage

def main():
  params = getSystemStatus()
  print(params)

if __name__ == "__main__":
  startTime = time.time()
  main()
  print(str(time.time()-startTime))

