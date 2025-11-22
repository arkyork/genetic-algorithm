from ga import GA


ga = GA()
best = ga.run()
print("\nFinal Solution:", best, "=", int(best, 2), "→", int(best, 2)**2)
