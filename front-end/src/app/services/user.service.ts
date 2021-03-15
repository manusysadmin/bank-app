import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

const BASE_URL = 'http://localhost:8000/api/manage/users';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor(private http: HttpClient) { }

  getAll(): Observable<any> {
    return this.http.get(`${BASE_URL}`);
  }

  get(id: string): Observable<any> {
    return this.http.get(`${BASE_URL}/${id}`);
  }

  update(id: string, data: any): Observable<any> {
    return this.http.put(`${BASE_URL}/${id}`, data);
  }

  delete(id: string): Observable<any> {
    return this.http.delete(`${BASE_URL}/${id}`);
  }
}
