import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { map } from 'rxjs/operators';
import { environment } from '../../environments/environment';

@Injectable({
    providedIn: 'root'
})
export class AuthService {
    constructor(private http: HttpClient) { }

    private authUrl = environment.baseUrl + '/api/v1/auth/';

    public getAuthToken(): string {
        return localStorage.getItem('access_token');
    }

    public getRefreshToken(): string {
        return localStorage.getItem('refresh_token');
    }

    login(username: string, password: string) {
        return this.http.post<any>(this.authUrl, { "username": username, "password": password })
            .pipe(map(user => {
                // login successful if there's a jwt token in the response
                if (user && user.access_token) {
                    // store user details and jwt token in local storage to keep user logged in between page refreshes
                    localStorage.setItem('username', JSON.stringify(user.username));
                    localStorage.setItem('access_token', JSON.stringify(user.access_token));
                    localStorage.setItem('refresh_token', JSON.stringify(user.refresh_token));

                }

                return user;
            }));
    }

    refreshToken() {
        const httpOptions = {
            headers: new HttpHeaders({
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + localStorage.getItem("refresh_token")
            })
        };

        return this.http.post<any>(this.authUrl + "refresh", {}, httpOptions)
            .pipe(map(resp => {
                if (resp && resp.access_token) {
                    localStorage.setItem('access_token', JSON.stringify(resp.access_token));
                }
                return resp;
            }));
    }

    logout() {
        // remove user from local storage to log user out
        localStorage.removeItem('username');
        localStorage.removeItem('access_token');
        localStorage.removeItem('refresh_token');
    }
}
