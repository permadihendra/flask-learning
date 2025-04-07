import axios from 'axios';

const API_URL = 'http://127.0.0.1:5000/api/v1';

// Function to handle errors
const handleErrors = (error) => {
  if (error.response) {
    // The request was made and the server responded with a status code
    console.error('API Error:', error.response.status, error.response.data);
  } else if (error.request) {
    // The request was made but no response was received
    console.error('API Error: No response received', error.request);
  } else {
    // Something else happended while making the request
    console.error('API Error:', error.message);
  }
  throw error;
};

// Function to set headers with Content-type: application/json
const setHeaders = () => {
  axios.defaults.headers.common['Content-Type'] = 'application/json';
};

// Function to get speakers
const getSpeakers = async () => {
  try {
    setHeaders();
    const response = await axios.get(`${API_URL}/speakers`);
    return response.data;
  } catch (error) {
    handleErrors();
  }
};

export default getSpeakers;
