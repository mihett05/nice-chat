import { api } from './index';

export interface AuthResponse {
  access_token: string;
  user_id: number;
  username: string;
}

export const login = async (username: string, password: string): Promise<AuthResponse | null> => {
  try {
    const formData = new FormData();
    formData.append('username', username);
    formData.append('password', password);
    const response = await api.post<AuthResponse>('/auth/login', formData);
    if (response.status !== 200) {
      return null;
    }
    localStorage.setItem('access_token', response.data.access_token);
    return response.data;
  } catch (e) {
    return null;
  }
};

export const register = async (username: string, password: string): Promise<AuthResponse | null> => {
  try {
    const response = await api.post<AuthResponse>('/auth/register', {
      username,
      password,
    });
    if (response.status !== 200 && response.status !== 201) {
      return null;
    }
    localStorage.setItem('access_token', response.data.access_token);
    return response.data;
  } catch (e) {
    return null;
  }
};
