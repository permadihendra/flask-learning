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

// Helper
const addHeaders = () => ({
  'Content-Type': 'multipart/form-data',
});

// Function to get speakers
const getSpeakers = async () => {
  try {
    const response = await axios.get(`${API_URL}/speakers/`, {
      headers: addHeaders(),
    });
    return response.data;
  } catch (error) {
    console.error('Error fetching speakers:', error.response?.data || error.message);
    handleErrors(error); // ✅ pass error into handleErrors
  }
};

// Add Speaker function
const addSpeaker = async (speakerData) => {
  const url = `${API_URL}/speakers/`;
  return axios
    .post(url, speakerData, { headers: addHeaders() })
    .then((response) => response.data)
    .catch(handleErrors);
};

export default { getSpeakers, addSpeaker };
