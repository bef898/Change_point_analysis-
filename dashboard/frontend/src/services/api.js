import axios from 'axios';

const API_BASE_URL = 'http://localhost:5000/api';

export const fetchPriceTrends = async (startDate, endDate) => {
  try {
    const response = await axios.get(`${API_BASE_URL}/price-trends`, {
      params: {
        start_date: startDate,
        end_date: endDate,
      },
    });
    return response.data;
  } catch (error) {
    console.error('Error fetching price trends:', error);
    throw error;
  }
};
