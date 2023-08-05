
from cloudvision.Connector.grpc_client import GRPCClient, create_query

token = "eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJkaWQiOjY5NDAzMTY2MTY1ODAzNDYzODQsImRzbiI6Im1jZ3JhdGhjIiwiZHN0IjoidXNlciIsImVtYWlsIjoibWNncmF0aGNAYXJpc3RhLmNvbSIsImV4cCI6MTY2MzA2Mjk1OCwiaWF0IjoxNjYyOTc2NTU4LCJzaWQiOiIzYThkNGEyZTA4YTEwNjU3YWZkMWU3ZGFiZTU4MmY4ZjIyZTdkMTlhYjMzYTU4NGNkYWYwNWIwZjE3MjE3ZjE3LXZjMXY4NVNhRmZRc0R6T1prbEFzOElMN1BIcHBQWXU5dzc1dmY0dW4ifQ.uRsdur4coECR8ng1LsYJfSRPm4GxaDiYMG7VhpdBwDRK5fi5QzvCyWhVb7z9wCD9MvTlaH9LKXnPS8qlXPLBAQ"
with GRPCClient("www.cv-dev.corp.arista.io:443", tokenValue=token) as client:

    ds = "JPE17191574"
    pe = ["Sysdb", "cell", "1", "routing", "bgp", "export", "vrfBgpPeerInfoStatusEntryTable",
          "default", "bgpPeerInfoStatusEntry", "172.20.253.20"]

    query = [
        create_query([(pe, ["sentOpenMsg"])], ds)
    ]
    for batch in client.get(query):
        for notif in batch["notifications"]:
            print(notif)
