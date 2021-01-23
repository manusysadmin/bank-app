import { Injectable } from '@angular/core';

const TOKEN_KEY = 'auth-token';
const USER_KEY = 'auth-user';

@Injectable({
  providedIn: 'root'
})
export class TokenStorageService {

  constructor() { }

  set token(token: string) {
    this._token = token;
  }

  get token(): string {
    return this._token;
  }

  isLoggedIn(): any {
    return this.token != null;
  }
}
