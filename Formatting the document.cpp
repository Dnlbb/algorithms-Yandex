#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <fstream>

using namespace std;

enum Type_obj {
	word, 
	embedded,
	surrounded,
	floating
};

class Obj {
public:
	Type_obj type_obj;
	int width, height;
	int dx, dy;

	Obj(int x, int y) {
		type_obj = Type_obj::word;
		width = x;
		height = y;
	}
	Obj() {}
};

void set_param_image(vector<vector<Obj>>& obj_file, string &word, string &param) {
	if (word == "height")
		obj_file.back().back().height = stoi(param);
	else if (word == "width")
		obj_file.back().back().width = stoi(param);
	else if (word == "layout") {
		if (param == "embedded")
			obj_file.back().back().type_obj = Type_obj::embedded;
		else if (param == "surrounded")
			obj_file.back().back().type_obj = Type_obj::surrounded;
		else
			obj_file.back().back().type_obj = Type_obj::floating;
	}
	else if (word == "dx")
		obj_file.back().back().dx = stoi(param);
	else if (word == "dy")
		obj_file.back().back().dy = stoi(param);
}

void create_fragment(vector <pair<int, Obj>>& parts, queue <int>& fragments, queue <int> &offset_fargments, int w, int &y, int h) {
	if (parts.empty()) {
		fragments.push(w);
		offset_fargments.push(0);
		y += h;
	}
	else {
		int count = 0;
		int x = 0;

		for (int i = 0; i < parts.size(); i++) {
			parts[i].second.height -= h;
			if (parts[i].second.height <= 0)
				count++;
		}

		while (count > 0) {
			for (auto i = parts.begin(); i < parts.end(); i++) {
				if ((*i).second.height <= 0) {
					parts.erase(i);
					count--;
					break;
				}
			}
		}
		
		for (int i = 0; i < parts.size(); i++) {
			if (parts[i].first - x > 0) {
				fragments.push(parts[i].first - x);
				offset_fargments.push(x);
			}
			x = parts[i].first + parts[i].second.width;
		}
		if (w - x > 0) {
			fragments.push(w - x);
			offset_fargments.push(x);
		}
		
		y += h;
	}
}

void insert_part(vector <pair<int, Obj>>& parts, Obj image, int x) {
	bool flag = false;
	for (auto i = parts.begin(); i < parts.end(); i++) {
		if ((*i).first > x) {
			parts.insert(i, { x, image });
			flag = true;
			break;
		}
	}
	if (!flag)
		parts.push_back({ x, image });
}

int main(){
	vector<pair<int, int>> res;


	ifstream in("input.txt");
	vector<string> file;
	string st;

	while (!in.eof()) {
		getline(in, st);
		file.push_back(st);
	}

	in.close();


	string arr[3];
	int w, h, c;
	int k = 0;

	for (char i : file[0]) {
		if (i == ' ')
			k++;
		else
			arr[k] += i;
	}

	w = stoi(arr[0]);
	h = stoi(arr[1]);
	c = stoi(arr[2]);

	vector<vector<Obj>> obj_file;
	obj_file.push_back(vector<Obj>());
	bool flag = false;
	string word;
	string param;
	bool fparam = false;

	for (int i = 1; i < file.size(); i++) {

		if (file[i] == "")
			obj_file.push_back(vector<Obj>());
		else {

			word = "";

			for (char j : file[i]) {

				if (j == '(') {
					flag = true;
					obj_file.back().push_back(Obj());
				}

				else if (j == ')'){
					set_param_image(obj_file, word, param);
					word = "";
					param = "";
					fparam = false;
					flag = false;
				}

				else if (j == ' ') {

					if (!word.empty()) {

						if (!flag)
							obj_file.back().push_back(Obj(c * word.size(), h));

						else
							set_param_image(obj_file, word, param);
						word = "";
						param = "";
						fparam = false;
					}
				}

				else {

					if (flag) {

						if (fparam)
							param += j;

						else {

							if (j == '=')
								fparam = true;

							else
								word += j;
						}
					}

					else
						word += j;
				}
					
			}

			if (!word.empty()) {

				if (flag) {
					set_param_image(obj_file, word, param);
					word = "";
					param = "";
					fparam = false;
				}
				else
					obj_file.back().push_back(Obj(c * word.size(), h));
			}
		}
	}

	vector <pair<int, Obj>> parts;
	queue <int> fragments;
	queue <int> offset_fargments;

	int x = 0, y = 0, current_h, last_x = 0, last_y = 0;
	int offset = 0;

	for (auto paragraph : obj_file) {
		if (paragraph.empty()) {
			y += h;
		}
		else {
			current_h = h;
			create_fragment(parts, fragments, offset_fargments, w, y, 0);
			offset = 0;
			last_x = 0;
			last_y = y;
			for (auto elem : paragraph) {
				if (elem.type_obj == Type_obj::word) {
					flag = false;
					while (!flag) {
						while (!fragments.empty()) {
							if (elem.width + offset < fragments.front()) {
								flag = true;
								fragments.front() -= elem.width + offset;
								last_x = offset_fargments.front() + elem.width + offset;
								last_y = y;
								offset_fargments.front() += elem.width + offset;
								offset = c;
								break;
							}
							else if (elem.width + offset == fragments.front()) {
								flag = true;
								last_x = offset_fargments.front() + elem.width + offset;
								last_y = y;
								fragments.pop();
								offset_fargments.pop();

								offset = 0;
								break;
							}
							else {
								fragments.pop();
								offset_fargments.pop();
								offset = 0;
							}
								
						}
						if (!flag) {
							create_fragment(parts, fragments, offset_fargments, w, y, current_h);
							current_h = h;
						}
							
					}
				}
				else if (elem.type_obj == Type_obj::embedded) {
					flag = false;

					while (!flag) {
						while (!fragments.empty()) {
							if (elem.width + offset < fragments.front()) {
								flag = true;
								fragments.front() -= elem.width + offset;
								last_x = offset_fargments.front() + elem.width + offset;
								last_y = y;
								res.push_back({ offset_fargments.front() + offset, y});
								offset_fargments.front() += elem.width + offset;
								offset = c;
								if (elem.height > current_h) {
									current_h = elem.height;
								}
								break;
							}
							else if (elem.width + offset == fragments.front()) {
								flag = true;
								last_x = offset_fargments.front() + elem.width + offset;
								last_y = y;
								res.push_back({ offset_fargments.front() + offset, y });
								fragments.pop();
								offset_fargments.pop();
								if (elem.height > current_h) {
									current_h = elem.height;
								}
								offset = 0;
								break;
							}
							else {
								fragments.pop();
								offset_fargments.pop();
								offset = 0;
							}

						}
						if (!flag) {
							create_fragment(parts, fragments, offset_fargments, w, y, current_h);
							current_h = h;
						}
					}

				}
				else if (elem.type_obj == Type_obj::surrounded) {
					offset = 0;
					flag = false;
					while (!flag) {
						while (!fragments.empty()) {
							if (elem.width < fragments.front()) {
								flag = true;
								last_x = offset_fargments.front() + elem.width;
								last_y = y;
								res.push_back({ offset_fargments.front(), y });
								insert_part(parts, elem, offset_fargments.front());
								fragments.front() -= elem.width;
								offset_fargments.front() += elem.width;
								break;
							}
							else if (elem.width == fragments.front()) {
								flag = true;
								last_x = offset_fargments.front() + elem.width;
								last_y = y;
								res.push_back({ offset_fargments.front(), y });
								insert_part(parts, elem, offset_fargments.front());
								fragments.pop();
								offset_fargments.pop();
								break;
							}
							else {
								fragments.pop();
								offset_fargments.pop();
							}
						}
						if (!flag) {
							create_fragment(parts, fragments, offset_fargments, w, y, current_h);
							current_h = h;
						}
					}
				}
				else if (elem.type_obj == Type_obj::floating){
					if (elem.dx + elem.width + last_x > w)
						res.push_back({ w - elem.width, last_y + elem.dy });
					else {
						if (elem.dx + last_x < 0)
							res.push_back({ 0, last_y + elem.dy });
						else
							res.push_back({ last_x + elem.dx, last_y + elem.dy });
					}
					last_y = res.back().second;
					last_x = res.back().first + elem.width;
				}
			}
			int max_h = current_h;
			for (int i = 0; i < parts.size(); i++) {
				if (parts[i].second.height > max_h)
					max_h = parts[i].second.height;
			}
			y += max_h;
			parts.clear();

			while (!fragments.empty()) {
				fragments.pop();
			}
			while (!offset_fargments.empty()) {
				offset_fargments.pop();
			}
		}
	}

	for (auto i : res)
		cout << i.first << " " << i.second << endl;

	return 0;
}
