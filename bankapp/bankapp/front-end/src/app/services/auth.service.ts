import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { tap, shareReplay } from 'rxjs/operators';
import jwt_decode from 'jwt-decode';
import * as moment from 'moment';

import { JwtPayload } from '../model/jwt-payload';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  private apiRoot = 'http://localhost:8000/api/';

  constructor(private http: HttpClient) {}

  private setSession(authResult: any): any {
    const token = authResult.token;
    const payload = jwt_decode(token) as JwtPayload;
    const expiresAt = moment.unix(payload.exp);

    localStorage.setItem('token', authResult.token);
    localStorage.setItem('expires_at', JSON.stringify(expiresAt.valueOf()));
  }

  get token(): any {
    return localStorage.getItem('token');
  }

  login(username: string, password: string): any {
    return this.http.post(
      this.apiRoot.concat('login/'),
      { username, password })
        .pipe(
          tap(response => this.setSession(response)),
          shareReplay(),
    );
  }

  register(username: string, password1: string, password2: string): any {
    return this.http.post(
      this.apiRoot.concat('register/'),
      { username, password1, password2 }
    ).pipe(
      tap(response => this.setSession(response)),
      shareReplay(),
    );
  }

  logout(): any {
    localStorage.removeItem('token');
    localStorage.removeItem('expires_at');
  }

  refreshToken(): any {
    if (moment().isBetween(this.getExpiration().subtract(1, 'days'), this.getExpiration())) {
      return this.http.post(
        this.apiRoot.concat('refresh-token/'),
        { token: this.token }
      ).pipe(
        tap(response => this.setSession(response)),
        shareReplay(),
      ).subscribe();
    }
  }

  getExpiration(): any {
    const expiration = localStorage.getItem('expires_at');
    if (expiration != null) {
      const expiresAt = JSON.parse(expiration);
      return moment(expiresAt);
    }
  }

  isLoggedIn(): any {
    return moment().isBefore(this.getExpiration());
  }

  isLoggedOut(): any {
    return !this.isLoggedIn();
  }
}
