module.exports = function(api) {
  api.cache(true);
  return {
    presets: [
      ['babel-preset-expo', { jsxImportSource: 'nativewind' }],
      'nativewind/babel'
    ],
    plugins: [
      // If you're using Reanimated, include its plugin as well
      'react-native-reanimated/plugin',
    ],
  };
};
