import axios from 'axios';

const baseApi = import.meta.env.VITE_API_URL;

export const getAuthHeaders = (): Record<string, string> => {
  const accessToken = localStorage.getItem('access_token');
  if (accessToken) {
    return {
      Authorization: `Bearer ${accessToken}`,
    };
  }
  return {};
};

export const api = axios.create({
  baseURL: baseApi,
  withCredentials: true,
});

api.interceptors.request.use((config) => ({
  ...config,
  headers: {
    ...config.headers,
    ...getAuthHeaders(),
  },
}));
