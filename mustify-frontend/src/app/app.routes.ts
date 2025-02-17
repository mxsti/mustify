import { Routes } from '@angular/router';
import {SongInfoPageComponent} from './songs/song-info-page/song-info-page.component';
import {AppComponent} from './app.component';

export const routes: Routes = [
  {
    path: 'songs',
    component: SongInfoPageComponent
  },
  {
    path: '',
    component: AppComponent
  },
];
