import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class TokenService {

  private _token: string = null;
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
