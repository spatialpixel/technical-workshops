// name: get_current_weather
// description: Tells the current weather given a location
// parameter: location (string) - The location the user is asking about.
// parameter: latitude (number) - The latitude of the location the user is asking about. (required)
// parameter: longitude (number) - The longitude of the location the user is asking about. (required)

// https://open-meteo.com/

const url = `https://api.open-meteo.com/v1/forecast?latitude=${args.latitude}&longitude=${args.longitude}&current=temperature_2m,relative_humidity_2m,wind_speed_10m,precipitation,rain,showers,snowfall`;

const result = await fetch(url);
const response = await result.json();

return response;
