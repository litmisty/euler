./build.makefiles/Makefile:
		@gyp build/euler.gyp --depth=. -f make --generator-output=./build.makefiles

./build.xcodefiles:
		@gyp build/euler.gyp --depth=. -f xcode --generator-output=./build.xcodefiles

xcode: ./build.xcodefiles
		@xcodebuild -project build.xcodefiles/build/euler.xcodeproj

clean:
		rm -rf ./build.xcodefiles
		rm -rf ./build.makefiles		