export interface IUser {
  id: number;
  username: string;
}

export class User implements IUser {
  constructor(public id: number, public username: string) {}
}
