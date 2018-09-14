import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { News } from './news';
import { MessagesService } from '../messages/messages.service';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { catchError, map, tap } from 'rxjs/operators';
import { environment } from '../../environments/environment';

const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};

@Injectable({
  providedIn: 'root'
})
export class NewsService {

  private newsUrl = environment.baseUrl + '/api/v1/news/';
 
  constructor(
    private http: HttpClient,
    private messagesService: MessagesService) { }

  getNews(): Observable<News[]> {
    return this.http.get<News[]>(this.newsUrl)
      .pipe(
        tap(news => this.log('fetched news')),
        catchError(this.handleError('getNews', []))
      );
  }

  addNews (news: News): Observable<News> {
    return this.http.post<News>(this.newsUrl, news, httpOptions).pipe(
      tap((news: News) => this.log(`added news w/ id=${news.id}`)),
      catchError(this.handleError<News>('addHero'))
    );
  }

  /**         
   * 
   */

  private log(message: string) {
    this.messagesService.add(`NewsService: ${message}`);
  }

  /**
 * Handle Http operation that failed.
 * Let the app continue.
 * @param operation - name of the operation that failed
 * @param result - optional value to return as the observable result
 */
  private handleError<T>(operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {

      // TODO: send the error to remote logging infrastructure
      console.error(error); // log to console instead

      // TODO: better job of transforming error for user consumption
      this.log(`${operation} failed: ${error.message}`);

      // Let the app keep running by returning an empty result.
      return of(result as T);
    };
  }
}
