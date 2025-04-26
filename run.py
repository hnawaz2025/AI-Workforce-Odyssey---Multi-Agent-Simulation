from model import AIWFModel
import matplotlib.pyplot as plt

# Set up model
model = AIWFModel(N_workers=50, N_corporations=5, N_government=1, automation_level=0.8)

# Run it for 50 steps
for i in range(50):
    model.step()

# Plot results
data = model.datacollector.get_model_vars_dataframe()
data.plot()
plt.title("Unemployment Rate Over Time")
plt.xlabel("Step")
plt.ylabel("Unemployment Rate")
plt.show()
