server = {
    "name" : "mlflow-server",
    "cpu" : 78,
    "memory" : 90
}
if server["cpu"] > 80 :
    print("ALERT:",server["name"],"CPU is high")
else:
    print(server["name"], "is healthy")

if server["memory"] > 85 :
   print("ALERT:",server["name"], "Memory is high")
else:
   print(server["name"], "Memory is healthy")
