import { Injectable } from '@angular/core';
import {environment} from '../../environments/environment.development';
import {HttpClient} from '@angular/common/http';
import {SongInfo} from './song.model';

@Injectable({
  providedIn: 'root'
})
export class SongService {
  private baseUrl = environment.baseUrl;

  constructor(private http: HttpClient) {}

  getSongsInfo() {
    return this.http.get<SongInfo[]>(`${this.baseUrl}/songs`);
  }
}
