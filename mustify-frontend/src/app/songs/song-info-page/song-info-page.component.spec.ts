import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SongInfoPageComponent } from './song-info-page.component';

describe('SongInfoPageComponent', () => {
  let component: SongInfoPageComponent;
  let fixture: ComponentFixture<SongInfoPageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SongInfoPageComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SongInfoPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
