import lightkurve as lk
import numpy as np
import matplotlib.pyplot as plt

star_name=input("Enter star name: ")
print("searching for data.....")
search=lk.search_lightcurve(star_name)
if search is None or len(search)==0:
	print("No data found!")
	exit()
print("Downloading data.....")

try:
	 curve=search[0].download() #so that if there are more than 1 files by the same name, only the first one is considered
except:
	print("Could not download data.. Try checking the spelling")
	exit()
curve=curve.remove_nans()
curve=curve.normalize()#this means dividing the whole data by its avg so that it looks good and as a small number and to make it easier to plot a graph
time=curve.time.value
flux=curve.flux.value
mean_flux=np.mean(flux)
std_flux=np.std(flux)
threshold=mean_flux-3*std_flux #we chose this
transit_indices=np.where(flux<threshold)[0] #cuz the data was in the form of tuple, in order to get it out of it we use [0] as tuple's first element was the array

print("Possible transit points found: ", len(transit_indices))

plt.figure(figsize=(12,6))
plt.plot(time, flux, ".", markersize=2, label="Brightness")
if len(transit_indices)>0:
	plt.plot(time[transit_indices], flux[transit_indices], "ro", markersize=4, label="Possible Transit")
	
plt.xlabel("Time (days)")
plt.ylabel("Normalized Brightness (flux)")
plt.title("Light curve of "+star_name)
plt.legend()
plt.grid(True)
plt.show()


#Finding consecutive transit points
groups=[]
transit=[]
for number in transit_indices:
	if not transit or number==transit[-1]+1:
	   transit.append(number)
	else:
		if len(transit)>=3:
		groups.append(transit)
		transit=[number]

if len(current)>=3:
	groups.append(current)

#Orbital period
transit_times=[]
for group im groups:
	center=np.mean(time[group])
	transit_times.append(center)
	
if len(transit_times)>=2:
	period=np.mean(np.diff(transit_times))
	print(f"Estimated Period: {period:.2f} days")

#transit depth
depth = 1 - np.min(flux)
print(f"Transit Depth: {depth*100:.3f}%")

#radius
planet_radius_ratio=np.sqrt(depth)
print(f"Planet radius = {planet_radius_ratio:.3f} stellar radii")
star_radius=float(input("Star radius (in Solar Radii): "))
planet_radius=planet_radius_ratio*star_radius
print(f"Planet Radius ≈ {planet_radius:.3f} Solar Radii")
