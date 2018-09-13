import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-news',
  templateUrl: './news.component.html',
  styleUrls: ['./news.component.css']
})
export class NewsComponent implements OnInit {

  
  @Input() author: string;
  @Input() content: string;
  @Input() media: string;

  constructor() { }

  ngOnInit() {
  }

}
