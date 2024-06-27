// name: search_academic_commons
// description: Searches Columbia University's Academic Commons database for a given topic keyword and returns ten relevant results.
// parameter: keyword (string, required) - A keyword describing the topic being searched for.

// https://academiccommons.columbia.edu/developers

const objectToQueryString = obj => Object.keys(obj).map(key => encodeURIComponent(key) + '=' + encodeURIComponent(obj[key])).join('&');

const urlParams = objectToQueryString({
  search_type: 'keyword',
  page: 1,
  per_page: 10,
  sort: 'best_match',
  order: 'desc',
  q: args.keyword
});

const base = `https://academiccommons.columbia.edu/api/v1/search`;
const url = `${base}?${urlParams}`;

const response = await fetch(url);
return await response.json();