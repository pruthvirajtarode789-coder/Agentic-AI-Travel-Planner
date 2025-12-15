from agent.agent import plan_trip

if __name__ == "__main__":
    result = plan_trip("delhi", "nanded", 3, 19.15, 77.32)
    print(result)
