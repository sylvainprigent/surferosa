import { Component, OnInit } from '@angular/core';
import { NewsService } from '../news.service';
import { News } from '../news';

@Component({
  selector: 'app-newsfeed',
  templateUrl: './newsfeed.component.html',
  styleUrls: ['./newsfeed.component.css']
})
export class NewsfeedComponent implements OnInit {

  newslist: News[];  

  constructor(private newsService: NewsService) { }

  ngOnInit() {
    this.getNews();
  }

  getNews(): void {
    this.newsService.getNews()
        .subscribe(newslist => this.newslist = newslist);
  }

  addNews(name: string): void {
    name = name.trim();
    if (!name) { return; }
    this.newsService.addNews({ "content": name } as News)
      .subscribe(news => {
        this.newslist.push(news);
      });
  }

}
