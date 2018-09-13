import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ToolshedBarComponent } from './toolshed-bar.component';

describe('ToolshedBarComponent', () => {
  let component: ToolshedBarComponent;
  let fixture: ComponentFixture<ToolshedBarComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ToolshedBarComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ToolshedBarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
