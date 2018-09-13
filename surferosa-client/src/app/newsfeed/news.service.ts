import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { News } from './news';
import { MessagesService } from '../messages/messages.service';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { catchError, map, tap } from 'rxjs/operators';

export const NEWS: News[] = [
  { id: '1', author: 'Sylvain Prigent', content: 'This is my first post' },
  { id: '2', author: 'Meriadec Prigent', content: 'This is my second post' },
  { id: '3', author: 'Paul Bismut', content: 'This is paul s post' },
];

@Injectable({
  providedIn: 'root'
})
export class NewsService {

  private newsUrl = ':8081/api/v1/news/';
 
  constructor(
    private http: HttpClient,
    private messagesService: MessagesService) { }

  getNews(): Observable<News[]> {
    return this.http.get<News[]>(this.newsUrl)
      .pipe(
        tap(heroes => this.log('fetched news')),
        catchError(this.handleError('getNews', []))
      );
  }

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
