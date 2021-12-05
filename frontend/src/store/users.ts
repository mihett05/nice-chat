import { createStore, createEvent, createEffect, forward } from 'effector';
import { IUser, User } from '../models/user';
import { getMe, getUser } from '../api/users';

type UsersState = {
  user: IUser | null;
  users: IUser[];
};

export const fetchUser = createEvent<number>();
export const fetchMe = createEvent();

const fetchUserFx = createEffect(async (id: number) => {
  const result = await getUser(id);
  if (result === null) return result;
  return new User(result.user_id, result.username);
});

const fetchMeFx = createEffect(async () => {
  const result = await getMe();
  if (result === null) return result;
  return new User(result.user_id, result.username);
});

forward({
  from: fetchUser,
  to: fetchUserFx,
});

forward({
  from: fetchMe,
  to: fetchMeFx,
});

export const $users = createStore<UsersState>({
  user: null,
  users: [],
});

$users.on(fetchMeFx.doneData, (state, user) => ({
  ...state,
  user,
}));

$users.on(fetchUserFx.doneData, (state, user) => ({
  ...state,
  users: user ? [...state.users, user] : state.users,
}));

fetchMe();
