// name: compute_cycling_time
// description: Returns the time it takes to cycle between two given points, A to B, in seconds.
// parameter: pointA (array of numbers, required) - The longitude and latitude of the starting point A.
// parameter: pointB (array of numbers, required) - The longitude and latitude of the destination point B.

// https://docs.mapbox.com/api/navigation/directions/

const base = "https://api.mapbox.com/directions/v5/mapbox/cycling/";
const start = `${args.pointA[0]},${args.pointA[1]}`;
const dest = `${args.pointB[0]},${args.pointB[1]}`;
const token = "access_token=YOUR_TOKEN_HERE";
const url = `${base}${start};${dest}?${token}`;

const response = await fetch(url);
const data = await response.json();

const time = data.routes[0].duration;

return `${time} seconds`;
