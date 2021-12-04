import { api } from './index';

export interface UsersResponse {
  user_id: number;
  username: string;
}

export const getMe = async (): Promise<UsersResponse | null> => {
  try {
    if (localStorage.getItem('access_token') === null) {
      return null;
    }
    const response = await api.get<UsersResponse>('/users/me');
    return response.data;
  } catch (e) {
    return null;
  }
};

export const getUser = async (userId: number): Promise<UsersResponse | null> => {
  try {
    const response = await api.get<UsersResponse>(`/users/${userId}`);
    if (response.status === 404) {
      return null;
    }
    return response.data;
  } catch (e) {
    return null;
  }
};
