#include <stdlib.h>
#include <cassert>

int main() {
	assert(getenv("LD_LIBRARY_PATH") != NULL);
	return 0;
}

